import Message from "./Message";
// import "./MessageList.css";
import { MessageData } from "../Assets/MessageData";
import BigWidget from "./Layout/BigWidget";
function MessageList() {
  return (
    <>
      <BigWidget title="Messages">
        <div className="h-[350px] flex flex-col items-center gap-5">
          {MessageData.map((message, index) => {
            return (
              <Message
                key={index}
                logo={message.image}
                name={message.sender}
                description={message.desc}
              />
            );
          })}
        </div>
      </BigWidget>
    </>
  );
}

export default MessageList;
