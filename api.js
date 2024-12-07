const axios = require('axios');
var cryptlib = require('cryptlib');
 
 
 




 const  GetProfile =async (token)=> {
    const iv = "#GV^%^SUR&T*#Y*4";
    const key = cryptlib.getHashSha256(iv, 32)


    const user = { data: {} }
 
    let data = cryptlib.encrypt(JSON.stringify(user), key, iv);
    try {

        let result = await axios.post('https://api.membersgram.com/main/v1/getprofile',
            {
                "data": data

            },
            {
                headers: {
                    lan: '',
                    versionc: 31221,
                    market: 'WebAppP',
                    'Content-Type': 'application/json',
                    mainapitoken: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1YjkwM2I2Y2Q3YTJmMjMxNzUyOTQyZiIsImlhdCI6MTczMzI5ODM1MX0.TO4X0dROPHbf2YM5LbuwbNrRmtQQzf7SgTswy_vSv78'
                }
            },
        );

        let mydata = result.data
// console.log(result)
        let resultRegister = JSON.parse(cryptlib.decrypt(mydata, key, iv))
 
console.log(resultRegister.data.user.coins)
        // return (resultRegister)

    } catch (error) {
        console.log(error)
        // return ({ message: 'err in GetleagueListJoins Api'  })
    }
}
GetProfile()