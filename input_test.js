const start = require('./index.js');
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const ask = msg => new Promise(resolve => 
  rl.question(msg, response => resolve(response))
);


;


const main = async () => {
  const writer = await ask("Rate writer out of 24: ");
  const executive_producer = await ask("Rate executive producer out of 24: ");
  const budget = await ask("Rate budget out of 7: ");
  const diversity = await ask("Rate diversity out of 9: ");
  const genre = await ask("Rate genre out of 8: ");
  const story = await ask("Rate story out of 6: ");
  const lead_character = await ask("Rate lead character out of 5: ");
  const second_lead = await ask("Rate second lead out of 4: ");
  const tone = await ask("Rate tone out of 2: ");
  const ratings = await ask("Rating out of 5: ");
  const executive_10years = await ask("Rate Executive_10 out of 3: ");

  const array = [writer, executive_producer, budget, diversity, genre, story,
            lead_character,second_lead, tone, ratings, executive_10years];
  console.log(array);
  // Requiring fs module
  const fs = require("fs");

  var myObject = [];
  // Defining new data to be added
    let newData = {
        writer: writer,
        executive_producer: executive_producer,
        budget: budget,
        diversity: diversity,
        genre: genre,
        story: story,
        lead_character: lead_character,
        second_lead: second_lead,
        tone: tone,
        ratings: ratings,
        executive_10years: executive_10years,
    };
  // Adding the new data to our object
  myObject.push(newData);
  
  // Writing to our JSON file
  var newData2 = JSON.stringify(myObject);
  fs.writeFile("data2.json", newData2, (err) => {
    // Error checking
    if (err) throw err;
    console.log("New data added");
    start();

  });

  // r1.on('close',()=>{
  //   start();
  // });
  rl.close();
};

main();