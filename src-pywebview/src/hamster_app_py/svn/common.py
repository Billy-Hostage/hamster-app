import pysvn

wc_notify_action_map = {
    pysvn.wc_notify_action.add: 'A',
    pysvn.wc_notify_action.commit_added: 'A',
    pysvn.wc_notify_action.commit_deleted: 'D',
    pysvn.wc_notify_action.commit_modified: 'M',
    pysvn.wc_notify_action.commit_postfix_txdelta: None,
    pysvn.wc_notify_action.commit_replaced: 'R',
    pysvn.wc_notify_action.copy: 'c',
    pysvn.wc_notify_action.delete: 'D',
    pysvn.wc_notify_action.failed_revert: 'F',
    pysvn.wc_notify_action.resolved: 'R',
    pysvn.wc_notify_action.restore: 'R',
    pysvn.wc_notify_action.revert: 'R',
    pysvn.wc_notify_action.skip: 'skip',
    pysvn.wc_notify_action.status_completed: None,
    pysvn.wc_notify_action.status_external: 'X',
    pysvn.wc_notify_action.update_add: 'A',
    pysvn.wc_notify_action.update_completed: "WCUpdated",
    pysvn.wc_notify_action.update_delete: 'D',
    pysvn.wc_notify_action.update_external: 'X',
    pysvn.wc_notify_action.update_update: 'U',
    pysvn.wc_notify_action.annotate_revision: 'A',
}

# new in svn 1.4?
if hasattr( pysvn.wc_notify_action, 'locked' ):
    wc_notify_action_map[ pysvn.wc_notify_action.locked ] = 'locked'
    wc_notify_action_map[ pysvn.wc_notify_action.unlocked ] = 'unlocked'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_lock ] = 'failed_lock'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_unlock ] = 'failed_unlock'

# new in svn 1.5
if hasattr( pysvn.wc_notify_action, 'exists' ):
    wc_notify_action_map[ pysvn.wc_notify_action.exists ] = 'exists'
    wc_notify_action_map[ pysvn.wc_notify_action.changelist_set ] = 'changelist_set'
    wc_notify_action_map[ pysvn.wc_notify_action.changelist_clear ] = 'changelist_clear'
    wc_notify_action_map[ pysvn.wc_notify_action.changelist_moved ] = 'changelist_moved'
    wc_notify_action_map[ pysvn.wc_notify_action.foreign_merge_begin ] = 'foreign_merge_begin'
    wc_notify_action_map[ pysvn.wc_notify_action.merge_begin ] = 'merge_begin'
    wc_notify_action_map[ pysvn.wc_notify_action.update_replace ] = 'update_replace'

# new in svn 1.6
if hasattr( pysvn.wc_notify_action, 'property_added' ):
    wc_notify_action_map[ pysvn.wc_notify_action.property_added ] = 'property_added'
    wc_notify_action_map[ pysvn.wc_notify_action.property_modified ] = 'property_modified'
    wc_notify_action_map[ pysvn.wc_notify_action.property_deleted ] = 'property_deleted'
    wc_notify_action_map[ pysvn.wc_notify_action.property_deleted_nonexistent ] = 'property_deleted_nonexistent'
    wc_notify_action_map[ pysvn.wc_notify_action.revprop_set ] = 'revprop_set'
    wc_notify_action_map[ pysvn.wc_notify_action.revprop_deleted ] = 'revprop_deleted'
    wc_notify_action_map[ pysvn.wc_notify_action.merge_completed ] = 'merge_completed'
    wc_notify_action_map[ pysvn.wc_notify_action.tree_conflict ] = 'tree_conflict'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_external ] = 'failed_external'

# new in svn 1.7
if hasattr( pysvn.wc_notify_action, 'update_started' ):
    wc_notify_action_map[ pysvn.wc_notify_action.update_started ] = 'update_started'
    wc_notify_action_map[ pysvn.wc_notify_action.update_skip_obstruction ] = 'update_skip_obstruction'
    wc_notify_action_map[ pysvn.wc_notify_action.update_skip_working_only ] = 'update_skip_working_only'
    wc_notify_action_map[ pysvn.wc_notify_action.update_external_removed ] = 'update_external_removed'
    wc_notify_action_map[ pysvn.wc_notify_action.update_shadowed_add ] = 'update_shadowed_add'
    wc_notify_action_map[ pysvn.wc_notify_action.update_shadowed_update ] = 'update_shadowed_update'
    wc_notify_action_map[ pysvn.wc_notify_action.update_shadowed_delete ] = 'update_shadowed_delete'
    wc_notify_action_map[ pysvn.wc_notify_action.merge_record_info ] = 'merge_record_info'
    wc_notify_action_map[ pysvn.wc_notify_action.upgraded_path ] = 'upgraded_path'
    wc_notify_action_map[ pysvn.wc_notify_action.merge_record_info_begin ] = 'merge_record_info_begin'
    wc_notify_action_map[ pysvn.wc_notify_action.merge_elide_info ] = 'merge_elide_info'
    wc_notify_action_map[ pysvn.wc_notify_action.patch ] = 'patch'
    wc_notify_action_map[ pysvn.wc_notify_action.patch_applied_hunk ] = 'patch_applied_hunk'
    wc_notify_action_map[ pysvn.wc_notify_action.patch_rejected_hunk ] = 'patch_rejected_hunk'
    wc_notify_action_map[ pysvn.wc_notify_action.patch_hunk_already_applied ] = 'patch_hunk_already_applied'
    wc_notify_action_map[ pysvn.wc_notify_action.commit_copied ] = 'commit_copied'
    wc_notify_action_map[ pysvn.wc_notify_action.commit_copied_replaced ] = 'commit_copied_replaced'
    wc_notify_action_map[ pysvn.wc_notify_action.url_redirect ] = 'url_redirect'
    wc_notify_action_map[ pysvn.wc_notify_action.path_nonexistent ] = 'path_nonexistent'
    wc_notify_action_map[ pysvn.wc_notify_action.exclude ] = 'exclude'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_conflict ] = 'failed_conflict'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_missing ] = 'failed_missing'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_out_of_date ] = 'failed_out_of_date'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_no_parent ] = 'failed_no_parent'

# new in svn 1.7.1+?
if hasattr( pysvn.wc_notify_action, 'failed_locked' ):
    wc_notify_action_map[ pysvn.wc_notify_action.failed_locked ] = 'failed_locked'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_forbidden_by_server ] = 'failed_forbidden_by_server'
    wc_notify_action_map[ pysvn.wc_notify_action.skip_conflicted ] = 'skip_conflicted'

# new in svn 1.8
if hasattr( pysvn.wc_notify_action, 'update_broken_lock' ):
    wc_notify_action_map[ pysvn.wc_notify_action.update_broken_lock ] = 'update_broken_lock'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_obstruction ] = 'failed_obstruction'
    wc_notify_action_map[ pysvn.wc_notify_action.conflict_resolver_starting ] = 'conflict_resolver_starting'
    wc_notify_action_map[ pysvn.wc_notify_action.conflict_resolver_done ] = 'conflict_resolver_done'
    wc_notify_action_map[ pysvn.wc_notify_action.left_local_modifications ] = 'left_local_modifications'
    wc_notify_action_map[ pysvn.wc_notify_action.foreign_copy_begin ] = 'foreign_copy_begin'
    wc_notify_action_map[ pysvn.wc_notify_action.move_broken ] = 'move_broken'

# new in svn 1.9
if hasattr( pysvn.wc_notify_action, 'cleanup_external' ):
    wc_notify_action_map[ pysvn.wc_notify_action.cleanup_external ] = 'cleanup_external'
    wc_notify_action_map[ pysvn.wc_notify_action.failed_requires_target ] = 'failed_requires_target'
    wc_notify_action_map[ pysvn.wc_notify_action.info_external ] = 'info_external'
    wc_notify_action_map[ pysvn.wc_notify_action.commit_finalizing ] = 'commit_finalizing'
