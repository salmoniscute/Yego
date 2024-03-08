import React, { useEffect, useState } from "react";


const Wanyegongao= () =>{
const [data, setData] = useState([])

 const api = "https://soa.tainan.gov.tw/Api/Service/Get/36f23fb6-0404-4420-a278-d50a7c0353a5"
    useEffect(() => {
        fetch(api, {method: "GET"})
        .then(res => res.json())
        .then(res => {
            console.log('data', res.data)
            setData(res.data)
        })
    }, [])

    return(
        <div className="container">
            <div className="title">
                <h1>網站公告</h1>
            </div>
            <div className="announcementtitle">
                { data.map(d => {
                   return (
                        <div>
                        </div>
                   )
                }) }
            </div>


        </div>

    );
}





export default Wanyegongao;
