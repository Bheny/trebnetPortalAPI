function Credit({ credit }) {
  return (
    <div className="widget  bg-primary__blue text-white">
      <div className="text-2xl"> Credits</div>
      <div className="text-xl font-bold">{credit ? credit : "Null"}</div>
    </div>
  );
}

export default Credit;
