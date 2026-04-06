function getdata(callFun){
  console.log('----------------');
    setTimeout(()=>{
      const d = [1,2,3,4]
      callFun(d)
    },2000)
  }
  
  function callFun(data){
    console.log('data: ', data);
  }
  
  // getdata(callFun)
  
// 'interface' declarations can only be used in TypeScript files.ts(8006)

// interface User {
//   id: number;
//   name: string;
//   email: string;
// }

  // map function of array
  const num = [1,2,3,4,5,6]
  const d = num.map(n => n*2);
  console.log('d: ', d);

  // map on 
  
  const add = (a ,b) => a * b


  console.log(add(5,6));