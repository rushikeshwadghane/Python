// Demonstrates handling a Promise with then and catch.

function check(){
    return new Promise((resolve ,reject)=>{
        const data = [1,2]
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
