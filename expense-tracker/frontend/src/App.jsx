import { useState, useRef } from "react";
import { FileUp } from "lucide-react";

export default function App() {
  const [fileName, setFileName] = useState("");

  const handleInput = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      setFileName(file.name);
    } else {
      setFileName("");
    }
  };

  const fileInputRef = useRef(null);

  return (
    <section className="flex flex-col items-center justify-center gap-3">
      <h1 className="text-blue-500 text-3xl">지출내역 분석 프로그램</h1>
      <form className="flex flex-col gap-3 items-center">
        <label htmlFor="upload">
          <FileUp width={100} height={100} alt="파일 선택하기" />
        </label>
        <input
          id="upload"
          type="file"
          accept=".csv,.xlsx"
          className="hidden"
          onChange={handleInput}
          ref={fileInputRef}
        ></input>
        {fileName && <p>{fileName}</p>}
        <div className="flex felx-row gap-3">
          <button
            type="button"
            className="bg-gray-200 rounded-sm px-3 py-1"
            onClick={() => fileInputRef.current?.click()}
          >
            파일 업로드
          </button>
          <button type="button" className="bg-gray-200 rounded-sm px-3 py-1">
            선택 삭제
          </button>
        </div>
      </form>
    </section>
  );
}
