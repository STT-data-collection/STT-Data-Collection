import classesp from "./body.css";
import axios from "axios";
import React, { useState } from "react";

export const Body = () => {
  const [userData, setUserData] = useState({});
  const [file, setFile] = useState();

  function handleChange(event) {
    setFile(event.target.files[0]);
  }
  
  function handleSubmit(event) {
    // trackPromise(
    event.preventDefault()
    const url = "https://stt-amharic.azurewebsites.net/predict";
    const formData = new FormData();
    formData.append("file", file);
    formData.append("fileName", file.name);
    console.log(file.name);
    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };
    
    axios.post(url, formData, config).then((response) => {
      console.log(response.data.message);
      setUserData(response.data);
    }).catch((err)=>{
      console.log(err,"error here")
    });
  }
  

  return (
    <>
     <div className="bodys section__margin" id="wgpt3">
    <div className="bodys-feature">
        <h3>በስተቀኝ በኩል የሚገኘዎን ጽሑፍ ወደ ማይክሮፎኑ ያንብቡ</h3>
    </div>
   <div>
   <div className="bodys-div"/>
     <h3>ወይም የድምጽ ፋይል ያያይዙ</h3>

      <div>
      <div className={classesp.container}>
         <div className={classesp.upload}>
              <div>
                  <form onSubmit={handleSubmit}>                    
                    <input type="file" onChange={handleChange} />
                    <button type="submit">ያስገቡ</button>
                  </form>
              </div>
              <section>
              <p>{userData.message}</p>
              </section>
            </div>
      </div>
      </div>
    </div>
  </div>
     
    </>
  );
};