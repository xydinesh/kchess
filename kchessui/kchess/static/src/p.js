/** @jsx React.DOM */
// The above declaration must remain intact at the top of the script.
var Simple = React.createClass({
    getInitialState: function () {
        return { count: 0 };
    },

    handleMouseDown: function () {
        alert(' I was told: ' + this.props.message);
        this.setState({ count: this.state.count + 1 });
    },

    render: function () {
        return React.DOM.div(null,
      React.DOM.div({ class: "clicker", onMouseDown: this.handleMouseDown },
        "Give me the message!"
      ),
      React.DOM.div({ class: "message" }, "Message conveyed: ",
        React.DOM.span({ class: "count" }, this.state.count), " time(s)")
    );
    }

});

React.renderComponent(Simple({ message: "Keep it simple" }),
                document.body);