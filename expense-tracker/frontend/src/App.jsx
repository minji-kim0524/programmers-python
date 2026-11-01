function App() {
  return (
    <section>
      <h1>지출내역 분석 프로그램</h1>
      <form className="flex flex-row gap-3 border-2">
        <label for="upload">파일 업로드:</label>
        <div className="border-4">
          <input
            id="upload"
            type="file"
            accept=".csv,.xlsx"
            placeholder="CSV 또는 XLSX 파일을 선택하세요"
          ></input>
        </div>
        <button type="button">업로드</button>
      </form>
    </section>
  );
}

export default App;
