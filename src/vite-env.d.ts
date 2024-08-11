/// <reference types="vite/client" />

declare namespace pywebview {
  let api: HamsterAppApi;

  interface HamsterAppApi {
    hello: () => Promise<string>
    svn_list: (absRepoUrl?: string) => Promise<any>
  }

}
