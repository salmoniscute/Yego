import {
    useState,
    ReactElement,
} from "react";

import "./index.scss";
const UserIcon = `${process.env.PUBLIC_URL}/assets/testUser.png`;

type propsType = Readonly<{

    parentID:string;

}>;

export default function DiscussionReplyArea(props: propsType): ReactElement {

    const [replyText, setReplyText] = useState<string>(""); 

    const {
        

    } = props;
    
    return (
        <div id="DiscussionReplyArea">
            <img src={UserIcon}/>
            <textarea
                placeholder="回覆內容"
                value={replyText}
                onChange={(e) => setReplyText(e.target.value)}
                rows={1}
            />
            
        </div>
    );
}
