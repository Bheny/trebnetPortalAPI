import { recentsData } from "../Assets/RecentsData";
import "./Recent.css";
function Recent() {
  return (
    <div className="bg-secondary__white w-full flex justify-center">
      <table className="md:w-[90%] w-full resize">
        <thead>
          <tr className="bg-secondary__white">
            <th className="px-5 py-3">Action</th>
            <th className="px-5 py-3">Time</th>
            <th className="px-5 py-3">Status</th>
          </tr>
        </thead>
        <tbody>
          {recentsData.map((data, index) => {
            return (
              <tr key={index} className="border-b-4 shadow bg-white">
                <td className="text-left px-5 py-3">{data.action}</td>
                <td className="text-center px-5 py-3">{data.time}</td>
                <td className="flex justify-center px-5 py-3 ">
                  <div
                    className={` text-center w-32 p-2 rounded shadow ${
                      data.status === 1
                        ? "bg-primary__accept"
                        : "bg-primary__decline"
                    }`}
                  >
                    {data.status === 1 ? "Successful" : "Failed"}
                  </div>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default Recent;
