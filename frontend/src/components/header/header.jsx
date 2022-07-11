import React from 'react';
import './header.css';
import ai from '../../assets/ai.webm'

const Header = () => (
  <div className="header section__padding" id="home">
    <div className="header-content">
      <h1 className="gradient__text">የአማርኛ ድምፅ መረጃ መሰብሰቢያ መሳሪያ</h1>
      <p>ይህ የአማርኛ ቋንቋ የመረጃ መሰብሰቢያ መሳሪያ ነው። ለፈቃደኝነትዎ እናመሰግናለን። ለቀረበው ጽሑፍ የድምጽ መረጃን ለመሰብሰብ ወደ ታችኛው ክፍል ይሂዱ፣<br></br>የተሰበሰበውን መረጃ ትክክለኛነት ለማረጋገጥ እባክዎ ቀጣዩን ቁልፍ ይጫኑ።</p>
      <div className="header-content__input">
        <button type="button">ጀምር</button>
      </div>
   </div>

    <div className="header-image">
      <video src={ai}loop muted autoPlay/>
    </div>
  </div>
);

export default Header;
