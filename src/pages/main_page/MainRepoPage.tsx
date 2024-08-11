import { RefreshCcw, ArrowDownToLine } from "lucide-react";
import { Panel, PanelGroup, PanelResizeHandle } from "react-resizable-panels";
import { Input } from "@/components/ui/input"
import { ChangeEvent, SetStateAction, useState } from "react";

// action buttons
const TOP_ACTION_ICON_SIZE = 26;
function TopActionButtons() {
  function onclick_Refresh() {
    console.log("refresh")
    // use api to call svn list
    pywebview.api.svn_list().then((a) => {
      console.log("done")
      console.log(a)
    })
  }
  function onclick_Update() {
    console.log("update")
  }

  return (
    <>
      <div className="flex flex-row gap-0 h-full">
        <div className="aspect-square hover:bg-cyan-400" onClick={onclick_Refresh}>
          <div className="flex flex-col gap-2 items-center justify-center h-full">
            <RefreshCcw size={TOP_ACTION_ICON_SIZE}/>
            <div>刷新</div>
          </div>
        </div>
        <div className="aspect-square  hover:bg-cyan-400" onClick={onclick_Update}>
          <div className="flex flex-col gap-2 items-center justify-center h-full">
            <ArrowDownToLine size={TOP_ACTION_ICON_SIZE}/>
            <div>同步</div>
          </div>
        </div>
      </div>
    </>
  )
}

function Addressbar(props: {
  value: string,
  setValue: React.Dispatch<SetStateAction<string>>
}) {
  function handleChange(e: ChangeEvent<HTMLInputElement>) {
    props.setValue(e.target.value);
  }
  return (
    <div className="ml-6 mr-6 items-center justify-center pt-1">
      <Input type="text" placeholder="路径..." value={props.value} spellCheck={false} onChange={handleChange} />
    </div>
  )
}

export function MainRepoPage() {
  const [addressbarValue, setAddressbarValue] = useState<string>("")

  return (
    <>
      <div className="h-screen select-none">
        <PanelGroup direction="vertical">
          <Panel defaultSize={10} minSize={10} maxSize={10}>
            <TopActionButtons />
          </Panel>
          <PanelResizeHandle className="h-0 pointer-events-none" disabled />
          <Panel defaultSize={6} minSize={6} maxSize={6}>
            <Addressbar value={addressbarValue} setValue={setAddressbarValue} />
          </Panel>
          <PanelResizeHandle className="h-0 pointer-events-none" disabled/>
          <Panel minSize={20}>
            <PanelGroup direction="horizontal" className="border">
              <Panel defaultSize={25} minSize={10}>
                <div>
                  Left
                </div>
              </Panel>
              <PanelResizeHandle className="w-1 bg-gray-500" />
              <Panel defaultSize={75} minSize={10}>
                <div>
                  Right
                </div>
              </Panel>
            </PanelGroup>
          </Panel>
          <PanelResizeHandle className="h-1 bg-gray-500" />
          <Panel defaultSize={20} minSize={10}>
            Command Logs
          </Panel>
          <Panel className="bg-purple-600" defaultSize={3} minSize={3} maxSize={3}>
            Status Bar
          </Panel>
        </PanelGroup>
      </div>
    </>
  )
}
