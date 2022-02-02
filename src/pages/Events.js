import { useState } from "react";
import { eventData } from "../Assets/EventData";
import Event from "../components/Event";
function Events() {
  const [events, setEvents] = useState(eventData);
  return (
    <div className="w-full h-full px-5 pt-3">
      {/* event bar */}
      <div className="bg-primary__blue grid grid-cols-2 px-5 py-3 w-full my-5 shadow rounded items-center ">
        <span className="font-bold text-xl w-full text-white">Events</span>

        <button className="px-3 bg-white rounded shadow text-primary__blue w-fit  py-2 place-self-end ">
          {events.length}
        </button>
      </div>

      <div className="flex mt-10 flex-row gap-y-10 gap-x-3 flex-wrap justify-self-stretch">
        {events.map((event, index) => {
          return <Event logo={event.image} title={event.title} key={index} />;
        })}
      </div>
    </div>
  );
}

export default Events;
