import axios from 'axios'
import React, { useState } from "react";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faTrashAlt,
  faExclamationCircle,
} from "@fortawesome/free-solid-svg-icons";
import useRecordingsList from "../../hooks/use-recordings-list";
import "./styles.css";

export default function RecordingsList({ audio }) {
  const { recordings, deleteAudio } = useRecordingsList(audio);
  const [ setUserData] = useState({});

  const [file, setFile] = useState();


  function handleChange(event) {
    setFile(event.target.files[0]);
  }
  function audioSubmit(event) {
    event.preventDefault();
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

    axios
      .post(url, formData, config)
      .then((response) => {
        console.log(response.data.success);
        setUserData(response.data);
      })
      .catch((err) => {
        console.log(err, "error here");
      });
  }

  return (
    <div className="recordings-container">
      {recordings.length > 0 ? (
        <>
          <h1>የተቀረጹ የድምጽ ፋይሎች</h1>
          <div className="recordings-list">
            {recordings.map((record) => (
              <div className="record" key={record.key}>
                <audio controls src={record.audio} />
                <div className="delete-button-container">
                  <button
                    className="delete-button"
                    title="Delete this audio"
                    onClick={() => deleteAudio(record.key)}
                  >
                    
                    <FontAwesomeIcon icon={faTrashAlt} />
                  </button>
                  <form onSubmit={audioSubmit}>
                      <button type="submit">ያስገቡ</button>
                    </form>{" "}
                </div>
              </div>
            ))}
          </div>
        </>
      ) : (
        <div className="no-records">
          <FontAwesomeIcon
            icon={faExclamationCircle}
            size="2x"
            color="#f2ea02"
          />
          <span>መዝገቦች የሉዎትም</span>
        </div>
      )}
    </div>
  );
}
