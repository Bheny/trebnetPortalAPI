import Job from "./Job";

import { jobData } from "../Assets/JobData.js";
function JobList() {
  return (
    <div className="flex flex-col gap-5 justify-center items-center w-fit sm:px-6">
      {jobData.map((job, index) => {
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
  );
}

export default JobList;
