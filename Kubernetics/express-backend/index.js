const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

let students = [
    {
        id:1,
        name:"Rahul",
        course:"MCA"
    },
    {
        id:2,
        name:"Priya",
        course:"BCA"
    }
];

app.get("/",(req,res)=>{
    res.send("Student API Running");
});

app.get("/students",(req,res)=>{
    res.json(students);
});

app.post("/students",(req,res)=>{

    const student={
        id:students.length+1,
        name:req.body.name,
        course:req.body.course
    };

    students.push(student);

    res.json(student);
});

app.listen(3000,()=>{
    console.log("Server running");
});