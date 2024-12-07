
var cryptlib = require('cryptlib');

var iv = "#GV^%^SUR&T*#Y*4";
var key = cryptlib.getHashSha256(iv, 32)


function decryptBody(data) {
    let result = JSON.parse(cryptlib.decrypt(data, key, iv));
    console.log(result)
}
function encryptBody(data) {
    let result = cryptlib.encrypt(JSON.stringify(data), key, iv).trim();
    console.log(result)
}


let register = {
    data: {
        phonenumber: "989373449122",
        tg_id: "387446175",
        market: "google"
    }
}

let verifyCode = {
    data : {
        "phonenumber" : "989373449122",
        "verifyCode" : 34106,
        "market" : "google"
    }
}
let getProfile = {
    data : {

    }
}
// let responseProfile = "NYwaXJVJlXDwlwANVGhs8iXYZ5uxHCFxnSTzu4r1ZQ2Za0a7SQr/pGjybqtBrweUMq6vbdclQcDUuooVUe0hCyZgPntByfn0nMwp7m5SBp+wnhf20glWGyBmAZexC7iLFWu4P34n89RnHOiNwjGGSD6W/y3A4OuoKoureOdLyst1k1Ya7y7YBSiFQ9Yf9lQzuoSAbHCP6v27OYb0V21nbvfL3wUKyTGQW5IrokgfW0FI1mdvb+NOkeGJWtdRB87RtLIDtkfmysrlPmwOqf3hLHx90ReEMkWd23tDAYqahqqJUbFO5vKf1tLcXFMBFtGVS5nJiI8QlmPBLC8h8L9wF7R6AkSJcRkFEaGNZ3UhpDhobWQYLvvzKrXxY167SRlnaaeWJcMC+vdjmsNs9Tz7/9DxuXtRG1KTUnsmfw5NYWwhtEYMrOrp0ULbcDza7MZZZLoIMLOlAGIi4F3Nbcg/qh9dHVsO1ogmcErSdeQr+5lKDBHnnta4U5hHt5hMGFmyDi/kWRba9v9TqUxMlM2XSCHtkJy3WRmCUmGTZT7Dq6+D5oRceBrBBVSwigg2KQEXRa609UoLMH35lDmnJXr/up2tlrLFEdIfyZj4tr2bhKgpVTLmuuBMbPwE97hvKZvaUagimVNgo5NNGl2nCxexsFR4Hh7aqztJZRnla4rLFnCH4sb2hS6P/UvOI0oYuHQUnHl9NV7c+qQNSI1p5CupKTZwrUtLL2IdU7bniEoxYW5zmhY3R48FTV1cV5z8jSIxQmVNr08AF7K3p2grcQ3yA+62z8yIli+MnF/byAZgPi46hafclh1ry74o6ssH4AAepjXXXQKEtW/CdqWmARi4hg=="


encryptBody(getProfile)

// decryptBody("NYwaXJVJlXDwlwANVGhs8iXYZ5uxHCFxnSTzu4r1ZQ2Za0a7SQr/pGjybqtBrweUjAAJecPETGaWHuD10vhuale4s04ql9oErg+HAWnp2IOdKljPqh6b7FXyYfN52UCGL4qQNvZg+yCc6eD15IYyrpekSRVcpRPjp51oxb/tJD6Ym1grmriZdrPme0rsrBz8X0mUqU0eC06bUDLehYK3jpKvRi+RRD85wRu2Iu188OJmhPfdd1C1CieUdL3ARscNs6WXQQLkRkoQqGBvjRxc2HlcBZwQZRUWKFB1bwO3lTorc3DmyisATWo8cQXPA/bZ2WOdTs7Lnb4agdnTg4E2DEZ/xNlnENTqwOEvvfoO1EnZKCXgIW/YBiYreQmIMXR+pvGCehFDKGlY2DENP/gXRB49FeqW/o3+11UInLSVQT4NeB0fUgFUnmrKkxwlLr4gyXlEBCY5M4iJC0VB/+j6Wf7yoXGlaXPV6h8F4H8QuGGgPXGW4H5gd02CQpG4x5D12ZoEyXjm2C/FHZ4hkXC4A0BSRqodj3pE/qdLux4PRpF2jlYVZBil0rhyDV0i6Dvr3vbA3nbqUyRfd8Hm3CeoeNHV/FV34G6wdBuCW8eXTxE=")