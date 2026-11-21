// Demonstrates asynchronous work with a Promise and async/await.

function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = "Data fetched";
            resolve(data);
        }, 2000);
    });
}

async function processData() {
    try {
        const data = await fetchData();
        console.log('data1: ', data);
        console.log("Processing:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}

processData();
