import classesp from "./body.css";
import axios from "axios";
import React, { useState } from "react";

export const Body = () => {
  const [userData, setUserData] = useState({});
  const [ setFile] = useState();

  function handleChange(event) {
    setFile(event.target.files[0]);
  }
  
  function handleSubmit(event) {
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
  

  return (
    <>
     <div className="bodys section__margin" id="wgpt3">
      <section>
        <div className="bodys-feature">
        <button type="submit">ጀምር</button>
         <h3>በስተቀኝ በኩል የሚገኘዎን ጽሑፍ ወደ ማይክሮፎኑ ያንብቡ</h3>
        </div>
      </section>
      <section>
        <div>
        <p>{userData.message}</p>
        </div>
      </section>
    
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