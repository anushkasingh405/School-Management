var React= require('react');
var ReactRouter = require('react-router');
var Router=ReactRouter.Router;
var Route= ReactRouter.Route;

var attendance=require('./attendance');
var marks=require('./marks');
var exam=require('./exam');
var Routes=(

    <Router>
        <Route path ="/teacher/attendance/" component={attendance}/>
        <Route path ="/teacher/marks/" component={marks}/>
        <Route path ="/teacher/exam/" component={exam}/>
    </Router>
);

module.exports=Routes;