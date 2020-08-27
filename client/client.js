const {SingleRequest, DoubleRequest, SingleReply} = require('./squares_pb.js');
const {CalculatorClient} = require('./squares_grpc_web_pb.js');

var client = new CalculatorClient('http://' + window.location.hostname + ':8080', null, null);

var request = new DoubleRequest();
request.setFirstNumber(16);
request.setSecondNumber(155);

client.addNumber(request, {}, (err, response) => {
    if (err) {
        console.log(`Unexpected error for squareNumber: code = ${err.code}, message = "${err.message}"`);
    } else {
        console.log(response.getResult());
    }
});