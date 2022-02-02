import { eventData } from "../Assets/EventData";
import BigWidget from "./Layout/BigWidget";
import Event from "./Event";
// import "./EventList.css";
function EventList() {
  return (
    <div>
      <BigWidget title=" Event List" name="events">
        <div className="w-full  h-[270px] grid place-items-center gap-5 py-5 md:px-4 ">
          {eventData.map((data, index) => {
            return <Event key={index} logo={data.image} title={data.title} />;
          })}
        </div>
      </BigWidget>
    </div>
  );
}

export default EventList;
