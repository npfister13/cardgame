To run, make sure you have some kind of webserver running

An easy one is "http-server", if you still have node installed
1. open a bash terminal window, enter ```npm install -g http-server```
2. it is now globally installed, you shouldnt ever have to run the npm install for this again
3. anytime you wanna spin up a simple web server, in a bash window run, ```http-server --cors```
4. it will start a webpage at, most likely, http://localhost:8080
5. remember to kill the server when you're done with ctrl+c