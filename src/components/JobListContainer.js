import { jobClass } from "../Assets/JobClass";
import { jobData } from "../Assets/JobData.js";
import "./JobListContainer.css";

import BigWidget from "./Layout/BigWidget";
import { useState } from "react";
import Job from "./Job";

function JobListContainer() {
  const [searchTerm, setSearchTerm] = useState("");
  const [searchClass, setSearchClass] = useState("");

  const filteredData = jobData.filter((job) => {
    if (searchTerm === "") {
      return job;
    } else if (job.title.toLowerCase().includes(searchTerm.toLowerCase())) {
      return job;
    }
  });

  const finalFilteredData = filteredData.filter((job) => {
    if (searchClass === "") {
      return job;
    } else if (job.class.toLowerCase().includes(searchClass.toLowerCase())) {
      return job;
    }
  });
  return (
    <>
      <BigWidget
        title="Jobs / Tasks"
        name="jobs"
        badge={finalFilteredData.length}
      >
        <div className="grid md:grid-cols-5 gap-5 w-full p-5 border-b-2 ">
          <input
            type="text"
            className="focus:border-blue-700 px-2 py-2 rounded shadow w-full md:col-span-3"
            placeholder="Search....."
            onChange={(e) => setSearchTerm(e.target.value)}
          />

          <select
            name="job-class"
            className="accent-blue-700 px-2 py-2 rounded shadow md:col-span-2 w-full"
            onChange={(e) => setSearchClass(e.target.value)}
          >
            <option value="">Filter by:</option>;
            {jobClass.map((jclass, index) => {
              return (
                <option value={jclass} key={index}>
                  Class {jclass}
                </option>
              );
            })}
          </select>
        </div>

        <div className="h-[350px] overflow-hidden overflow-y-scroll w-fit">
          {finalFilteredData && (
            <div className="flex flex-col gap-5 justify-center items-center w-fit sm:px-6">
              {finalFilteredData.map((job, index) => {
                return (
                  <Job
                    key={index}
                    logo={job.image}
                    title={job.title}
                    jclass={job.class}
                    description={job.desc}
                  />
                );
              })}
            </div>
          )}
        </div>
      </BigWidget>
    </>
  );
}

export default JobListContainer;

// function JobList() {
//   return (
//     <div className="flex flex-col gap-5 justify-center items-center w-fit sm:px-6">
//       {jobData.map((job, index) => {
//         return (
//           <Job
//             key={index}
//             logo={job.image}
//             title={job.title}
//             jclass={job.class}
//             description={job.desc}
//           />
//         );
//       })}
//     </div>
//   );
// }
