(function(win,body){
	function Dialog(opts){
		this.opts = $.extend({},Dialog.defaults,opts);
		this.render();
		this.bindEvent();
	}

	Dialog.prototype.mask = function(){
		var mask = $('<div class="ui-dialog-mask"></div>');
		this.mask = mask;
		$(body).append(mask);

	};

	Dialog.prototype.close = function(){
		var dialog = this.dialog, mask = this.mask;
		$(body).removeChild(dialog);

	};

	Dialog.prototype.bindEvent = function(){
		var self = this;
		this.closeBtn.on('click',function(){
			self.close();
		});
	};

	Dialog.prototype.render = function(){
		var opts = this.opts;
		this.dialog = $(opts.template);
		this.diaTitle = this.dialog.find('.ui-dialog-title');
		this.diaBody = this.dialog.find('.ui-dialog-content');
		this.closeBtn = this.dialog.find('.ui-dialog-close-btn');
		this.diaBody.html(opts.content);
		this.diaTitle.html(opts.title);
		this.dialog
		.addClass(opts.skinClassName)
		.appendTo(body);

		this.mask();

		
	};

	Dialog.defaults = {
		width: 400,
		height: 300,
		title:'',
		content: '',
		skinClassName:'',
		template: 
	  	'<div class="ui-dialog">'
		+  '<div class="ui-dialog-header">'
		+     '<div class="button"><a class="ui-dialog-close-btn"></a></div>'
		+     '<div class="ui-dialog-title"></div>'
		+  '</div>'
		+  '<div class="ui-dialog-body">'
		+     '<div class="ui-dialog-content"></div>'
		+  '</div>'
		+  '<div class="ui-dialog-footer"></div>'
		+'</div>'
	};


	win.Dialog = Dialog;


})(window,document.body);