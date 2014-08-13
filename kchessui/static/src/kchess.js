/** @jsx React.DOM */
// The above declaration must remain intact at the top of the script.
// Your code here	  
var KchessForm = React.createClass({
	handleSubmit: function() {
		var white = this.refs.white.getDOMNode().value.trim();
		var black = this.refs.black.getDOMNode().value.trim();
		var result = this.refs.result.getDOMNode().value.trim();
		var wtime = this.refs.wtime.getDOMNode().value.trim();
		var btime = this.refs.btime.getDOMNode().value.trim();
		var comment = this.refs.comment.getDOMNode().value.trim();
		this.props.onKchessSubmit({white: white, black: black, result:result,
			wtime: wtime, btime: btime, comments: comment});
	},
	render: function() {
		return <form className="kchessForm" onSubmit={this.handleSubmit}>
			    <input type="text" placeholder="White" ref="white"/>
		        <input type="text" placeholder="Black" ref="black"/>
		        <br/>
		        <br/>
		        <input type="text" placeholder="Result" ref="result"/>
		        <br/>
		        <input type="text" placeholder="White Time" ref="wtime"/>
		        <input type="text" placeholder="Black Time" ref="btime"/>
		        <br/>
		        <textarea rows="10" columns="10" placeholder="Comment" ref="comment"/>
		        <br/>
		        <input type="submit" value="Post"/>
		        <br/></form>;
    }
});
	  
var KchessBox = React.createClass({
	handleKchessSubmit: function(comment) {
		$.post({
			url: this.props.url,
			dataType: 'json',
			data: comment,
			success: function(data) {
				console.log(comment);
				this.setState({data: data});
			}.bind(this),
			error: function(xhr, status, err) {
				console.error(comment);
				console.error(JSON.stringify(xhr));
				console.error(this.props.url, status, err);
			}.bind(this)
		});
	},
	getInitialState: function() {
		return {data: []};
	},
	render: function() {
		return (
		  React.DOM.div({className: "kchessBox"},
		  <h1> Final Result </h1>,
		  <KchessForm onKchessSubmit={this.handleKchessSubmit}/>)
			);
}
});
	  

// instantiates root component, starts the framework and 
// injects the markup into raw DOM element.
React.renderComponent(
  <KchessBox url='/game/result'/>,
  document.getElementById('content')
		);