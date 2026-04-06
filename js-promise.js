function check(){
    return new Promise((resolve ,reject)=>{
        data = [1,2]
        resolve(data)

    })
}

check()
    .then((data)=>{
        console.log('data: ', data);

    })
    .catch((err)=>{
        console.log('err: ', err);

    });

check()
