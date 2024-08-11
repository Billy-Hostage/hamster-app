import pysvn

def svn_list(url: str, recursive: bool = False):
    client = pysvn.Client()
    isurl = client.is_url(url)
    assert isurl == 1
    all_entries = client.list(
        url,
        revision=pysvn.Revision( pysvn.opt_revision_kind.head ),
        recurse=recursive,
        fetch_locks=True,
        include_externals=False
    )
    paths: list[dict] = []
    for entry_tuple in all_entries:
        ent_obj = entry_tuple[0]
        lock_obj = entry_tuple[1]
        le_time_unix_float_sec: float = ent_obj.time
        # to int in ms
        le_time_unix_int_ms: int = int(le_time_unix_float_sec * 1000.0)

        serialized = {
            "absPath": ent_obj.path,
            "relPath": ent_obj.repos_path,
            "size": ent_obj.size,
            "lastAuthor": ent_obj.last_author,
            "type": "file" if ent_obj.kind == pysvn.node_kind.file else "dir" if ent_obj.kind == pysvn.node_kind.dir else "unknown",
            "lastEditAtUnixMs": le_time_unix_int_ms,

            "lockedBy": None
        }

        if lock_obj is not None:
            serialized["lockedBy"] = lock_obj.owner

        paths.append(serialized)

    return paths
