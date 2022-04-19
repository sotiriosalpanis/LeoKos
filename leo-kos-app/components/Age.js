import React from 'react'

const Age = () => {

  const birthday = new Date("12/29/2021");
  const age = Math.floor((Date.now() - birthday) / (1000 * 3600 * 24 * 7));
  const correctedBirthday = new Date("02/06/2022");
  const correctedAge = Math.floor((Date.now() - correctedBirthday) / (1000 * 3600 * 24 * 7));


  return (
    <div>
      <p>{`${age} weeks old`}</p>
      <p>{`(${correctedAge} corrected)`}</p>
    </div>
  )
}

export default Age