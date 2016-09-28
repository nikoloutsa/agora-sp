
var formName = 'Service Component Implementation Detail Form';

var serviceId = null;
var serviceDetailsId = null;
var componentImplementationDetailId = null;
var newServiceId = null;
var newServiceDetailsId = null;
var newComponentImplementationDetailId = null;
var opType = "";

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'service_id', placeholder: 'Enter service name', label: 'Service' },
	{ tag: 'input', type: 'text', name: 'service_details_id', label: 'Service details', placeholder: "Enter service version" },
	{ tag: 'input', type: 'text', name: 'component_implementation_detail_id', label: 'Component implementation detail', placeholder: "Enter component implementation detail version" }
];

var OptionsComponent = React.createClass({
	render: function(){
		var htmlOptions = this.props.options.map(function(option) {
      return(
      	<option value={option.value} key={option.id}>{option.text}</option>
      );
		});		
		return (
			<select name={this.props.selectName} id={this.props.selectName} className="form-control">
				{htmlOptions}
		  </select>
		);
	}
});

var FormWrapper;
FormWrapper = React.createClass({

	generateFormElements: function (resourceObject) {
		var formElements = resourceObject.map(function (field) {
			if (field.tag == 'input') {
				if (field.type == 'text') {
					return (
						<div className="form-group">
							<label htmlFor={field.name}>{field.label}</label>
							<input className="form-control" id={field.name} type={field.type} name={field.name}
								   placeholder={field.placeholder} aria-describedby={field.name + '-error'}/>
							<span id={field.name + '-error'} className="validation-message sr-only"></span>
						</div>
					);
				}
			}
			else if (field.tag == 'textarea') {
				return (
					<div className="form-group">
						<label htmlFor={field.name}>{field.label}</label>
						<textarea className="form-control" id={field.name} name={field.name}
								  placeholder={field.placeholder} rows="6" onChange={this[field.onChange]}></textarea>
						<span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);
			}
			else if (field.tag == 'select') {
				return (
					<div className="form-group">
						<label htmlFor={field.name}>{field.label}</label>
						<OptionsComponent options={field.optionsData} selectName={field.name}></OptionsComponent>
						<span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);
			}
		}, this);
		return formElements;
	},

	markInvalid: function (elRef, message) {
		$('#' + elRef).next().removeClass('sr-only');
		$('#' + elRef).next().html(message);
		$('#' + elRef).parent().addClass('has-error');
		$('html, body').animate({
			scrollTop: $('#' + elRef).offset().top
		}, 800);
	},

	clearValidations: function () {
		console.log("Clearing the validations");
		$('body').find('.has-error').removeClass('has-error');
		$('body').find('.validation-message').addClass('sr-only');
	},

	textareaHTMLValidation: function (e) {
		var div = document.createElement('div');
		div.innerHTML = $(e.target).val();
		if ($(div).find('script').length > 0 || $(div).find('link').length) {
			div = null;
			this.markInvalid($(e.target).attr('name'), 'This HTML content must not have script or css tags');
		}
		else {
			$(e.target).parent().removeClass('has-error');
			$(e.target).parent().find('.validation-message').addClass('sr-only');
		}
		div = null
	},

	validateForm: function (e) {
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = ''

		// --- validation code goes here ---
		var service = $('#service_id').val();
		if (service == '' || service == null) {
			validationMessage = "The service is required";
			validationObjects.push({field: 'service_id', message: validationMessage});
		}

		var service_details = $('#service_details_id').val();
		if (service_details == null || service_details == "") {
			validationMessage = "The service version is required.";
			validationObjects.push({field: 'service_details_id', message: validationMessage});
		}

		var comp_imp_det = $('#component_implementation_detail_id').val();
		if (comp_imp_det == null || comp_imp_det == "") {
			validationMessage = "The component implementation details are required.";
			validationObjects.push({field: 'component_implementation_detail_id', message: validationMessage});
		}

		if (validationObjects.length > 0) {
			var i = 0;
			for (i = 0; i < validationObjects.length; i++) {
				this.markInvalid(validationObjects[i].field, validationObjects[i].message);
			}
			return false;
		}

		return true;
	},

	handleSubmit: function (e) {
		// some validation
		// ajax url call + redirect
		e.preventDefault();

		if (this.validateForm()) {
			//var formValues = JSON.stringify($("#service-form").serializeJSON());
			//console.log("The form values are ->", formValues);

			var params = {};


			var parts = window.location.href.split("/");
			var host = "http://" + parts[2];
			var url = "";

			if (this.props.source != null && this.props.source != "") {

				params["component_implementation_details_uuid"] = componentImplementationDetailId;
				params["new_component_implementation_details_uuid"] = newComponentImplementationDetailId;
				params["service_id"] = serviceId;
				params["new_service_id"] = newServiceId;
				params["service_version"] = serviceDetailsId;
				params["new_service_version"] = $("#service_details_id").val();

				url = host + "/api/v1/component/service_details_component_implementation_details/edit";
				opType = "edit";
			}
			else {

				params["component_implementation_details_uuid"] = newComponentImplementationDetailId;
				params["service_id"] = newServiceId;
				params["service_version"] = $("#service_details_id").val();

				url = host + "/api/v1/component/service_details_component_implementation_details/add";
				opType = "add";
			}

			console.log(params);


			this.serverRequest = $.ajax({
				url: url,
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType: "application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if (opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new service details component relationship");
					else
						$("#modal-success-body").text("You have successfully updated the service details component relationship");
					$("#modal-success").modal('show');
				}.bind(this),
				error: function (xhr, status, err) {
					var response = JSON.parse(xhr.responseText);
					$("#modal-body").text(response.errors.detail);
					$("#modal-danger").modal('show');
				}.bind(this)
			});
		}
		else {
			console.log("The form is not valid");
		}

	},

	getInitialState: function () {
		return {
			component: {
				version: "",
				configuration_parameters: ""
			}
		}
	},

	componentDidMount: function () {

		if (this.props.source == null || this.props.source == "")
			return;

		jQuery.support.cors = true;
		this.serverRequest = $.ajax({
			url: this.props.source,
			dataType: "json",
			crossDomain: true,
			type: "GET",
			cache: false,
			success: function (data) {
				this.setState({component: data.data});
				$("#service_id").val(this.state.component.version);
				$("#service_details_id").val(this.state.component.configuration_parameters);
				$("#component_implementation_detail_id").val(this.state.component.service_component_implementation.name);

			}.bind(this),
			error: function (xhr, status, err) {
				console.log(this.props.source, status, err.toString());
			}.bind(this)
		});
	},

	componentWillUnmount: function () {
		this.serverRequest.abort();
	},

	render: function () {
		var formElements = this.generateFormElements(this.props.resourceObject);
		return (
			<div className="widget">
				<div className="widget-header bordered-bottom bordered-blue">
					<span className="widget-caption">{this.props.formName}</span>
				</div>
				<div className="widget-body">
					<form role="form" onSubmit={this.handleSubmit} id="service-form">
						{formElements}
						<button type="submit" className="btn btn-blue">Submit</button>
					</form>
				</div>
			</div>
		);
	}
});

ReactDOM.render(
  <FormWrapper resourceObject={resourceObject} formName={formName} source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);


$( function() {

	var temp = null;
	$(document).bind('click', function (event) {
        // Check if we have not clicked on the search box
        if (!($(event.target).parents().andSelf().is('#service_id'))) {
			$(".ui-menu-item").remove();
		}

		if (!($(event.target).parents().andSelf().is('#service_details_id'))) {
			$(".ui-menu-item").remove();
		}

		if (!($(event.target).parents().andSelf().is('#component_implementation_detail_id'))) {
			$(".ui-menu-item").remove();
		}});


	var getDataService = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/services/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
                response(data.data);
            });
	};

	var getDataServiceDetails = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];


		var service = $("#service_id").val();
		if(service == null)
			service = "";

        $.getJSON(
            host + "/api/v1/services/version/all?search=" + request.term + "&service=" + service,
            function (data) {
				console.log(data);
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].version;
					data.data[i].label = data.data[i].version;
                    data.data[i].index = i;
				}
                response(data.data);
            });
	};

    var getDataComponentImplementationDetail = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/component/implementation_detail/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].version;
					data.data[i].label = data.data[i].version;
                    data.data[i].index = i;
				}
                response(data.data);
            });
	};


    $( "#service_id" ).autocomplete({
      source: getDataService,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newServiceId = ui.item.uuid;
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  focus: function(event, ui){
          var items = $(".ui-menu-item");
		  items.removeClass("ui-menu-item-hover");
		  $(items[ui.item.index]).addClass("ui-menu-item-hover");
	  }
    }).autocomplete( "instance" )._renderItem = function( ul, item ) {
		return $( "<li>" )
        .append( item.name )
        .appendTo( ul );
    };

	$( "#service_details_id" ).autocomplete({
      source: getDataServiceDetails,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newServiceDetailsId = ui.item.uuid;
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  focus: function(event, ui){
          var items = $(".ui-menu-item");
		  items.removeClass("ui-menu-item-hover");
		  $(items[ui.item.index]).addClass("ui-menu-item-hover");
	  }
    }).autocomplete( "instance" )._renderItem = function( ul, item ) {
		return $( "<li>" )
        .append( item.service.name + " " + item.version )
        .appendTo( ul );
    };

    $( "#component_implementation_detail_id" ).autocomplete({
      source: getDataComponentImplementationDetail,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newComponentImplementationDetailId = ui.item.uuid;
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  focus: function(event, ui){
          var items = $(".ui-menu-item");
		  items.removeClass("ui-menu-item-hover");
		  $(items[ui.item.index]).addClass("ui-menu-item-hover");
	  }
    }).autocomplete( "instance" )._renderItem = function( ul, item ) {
		return $( "<li>" )
        .append( item.service_component.name + " " + item.service_component_implementation.name + " " + item.version )
        .appendTo( ul );
    };


  } );