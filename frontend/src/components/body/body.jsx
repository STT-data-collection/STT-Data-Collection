import classesp from "./body.css";
import axios from "axios";
import React, { useState } from "react";

export const Body = () => {
  const [userData, setUserData] = useState({});
  const [ file,setFile] = useState();

  function handleChange(event) {
    setFile(event.target.files[0]);
  }
  
  function handleClick(event) {
    event.preventDefault()
    const url = 'https://afri-speech-to-text.herokuapp.com/get-text';
    const config = {
      headers: { }
    };
    axios.get(url,  config).then((response) => {
      console.log(response.data.result);
      setUserData(response.data);

    }).catch((err)=>{
      console.log(err,"error here")
    });
  }
  function audioSubmit(event){
    event.preventDefault()
    const url = "https://afri-speech-to-text.herokuapp.com/send-audio";
    const formData = new FormData();
    formData.append("file", file);
    formData.append("YourFile", file.name);
    console.log(file.name);
    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };
    
    axios.post(url, formData, config).then((response) => {
      console.log(response.data.success);
      setUserData(response.data);
      
    }).catch((err)=>{
      console.log(err,"error here")
    });
  }
  return (
    <>
     {/* Get text */}
     <div className="bodys section__margin" id="wgpt3">
      <section>
      <form onClick={handleClick}>                    
        <div className="bodys-feature">
        <button type="click">ጀምር</button>
        </div>
        </form>
      </section>
      <section>
        <div>
        <h3>ከታች የሚገኘዎን ጽሑፍ ወደ ማይክሮፎኑ ያንብቡ</h3>
        <p>{userData.result}</p>
        </div>
      </section>
    <div>
    <div className="bodys-div"/>



    
    </div>
    {/* Upload audio */}
   <div>
   <div className="bodys-div"/>
   
     <h3>ወይም የድምጽ ፋይል ያያይዙ</h3>

      <div>
      <div className={classesp.container}>
         <div className={classesp.upload}>
              <div>
                  <form onSubmit={audioSubmit}>                    
                    <input type="file" onChange={handleChange} />
                    <button type="submit">ያስገቡ</button>
                  </form>
              </div>
              <section>
              <p>{userData.success}</p>
              </section>
            </div>
      </div>
      </div>
    </div>
  </div>
     
    </>
  );
};