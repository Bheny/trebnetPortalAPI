import { Send } from "@mui/icons-material";
// import "./Credits.css";
// import "../App.css";
import { transactionData } from "../Assets/TransactionData";
import { useAuth } from "../Contexts/AuthContext";
import { useState } from "react";

function Credits() {
  const { currentUser } = useAuth();
  const [credits, setCredits] = useState(currentUser.user_credit);
  return (
    <div className="w-full h-full px-5">
      {/* credit nav */}
      <div className="bg-primary__blue grid grid-cols-2 px-5 py-3 w-full my-5 shadow rounded items-center">
        <span className="font-bold text-xl w-full text-white">Credits</span>

        {currentUser.role === 1 && (
          <button className="px-3 bg-white rounded shadow text-primary__blue w-fit sm:w-[200px] py-2 place-self-end ">
            <span className="hidden md:inline-block mr-5">Send Credits</span>
            <Send />
          </button>
        )}
      </div>
      {/* total credits  */}
      <div className="bg-primary__blue px-10 py-5 my-5 text-white rounded shadow grid gap-5 place-self-start w-fit ">
        <div className="font-bold text-xl">Total Rcs</div>
        <div className="font-bold text-5xl">
          {credits}
          <small className="font-light text-lg ">.00</small>
        </div>
        <div className="text-lg font-bold">Rcs</div>
      </div>
      {/* transaction history */}

      <div className="grid w-full place-items-center shadow-lg pb-5 my-5 ">
        <span className="text-lg font-bold text-white bg-primary__blue px-5 py-4 w-full text-left rounded-tr rounded-tl">
          TRANSACTION HISTORY
        </span>
        <div className="w-full px-10 mt-3 h-56 overflow-y-scroll">
          <table className="w-full text-center table-auto border-collapse">
            <thead>
              <tr className="border-b-4 border-gray-500">
                <th colSpan="2" className="py-3 px-2">
                  Transaction ID
                </th>
                <th className="py-3 px-2">From</th>
                <th className="py-3 px-2">To</th>
                <th className="py-3 px-2">Current Bal</th>
                <th className="py-3 px-2">Amount</th>
                <th className="py-3 px-2">Balance</th>
              </tr>
            </thead>
            <tbody>
              {transactionData.map((transaction, index) => {
                return (
                  <tr key={index} className="border-b-2 border-gray-300 ">
                    <td className="py-3 px-2">
                      <input type="checkbox" name="transaction" id={index} />
                    </td>
                    <td className="py-3 px-2 text-left">
                      {transaction.transctionID}
                    </td>
                    <td className="py-3 px-2">{transaction.from}</td>
                    <td className="py-3 px-2">{transaction.to}</td>
                    <td className="py-3 px-2">{transaction.currentBalance}</td>
                    <td className="py-3 px-2">{transaction.Amount}</td>
                    <td className="py-3 px-2">{transaction.Balance}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Credits;
//w-full grid gap-5 px-7 place-items-center h-full pb-20
