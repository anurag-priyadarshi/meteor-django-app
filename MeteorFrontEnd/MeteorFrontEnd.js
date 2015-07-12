// basic routing using iron:router 
Router.route('/',{template: 'landing'});
Router.route('/ArticleDetail/',{
  template:'ArticleDetail'
  }
);

if (Meteor.isClient) {
  
  //Storing session related info in Session object
  
  Session.setDefault("getResponse", "");
  Session.setDefault("ArticleDetails", "");
  Session.setDefault("Recommendations", "");
  
  //helpers
  
  //helper for main template
  
  Template.main.helpers({
    recommendations: function () {
      return Session.get('Recommendations');
    },
    range: function(){
      return [0,1,2,3];
    }
    });
  
  //helper for landing template
  
  Template.landing.helpers({
    getResponse: function () {
      return Session.get('getResponse');
    }  
  });
  
  //helper for Article Detail template
  
  Template.ArticleDetail.helpers({
    title: function () {
      article = Session.get('ArticleDetails');
      return article.title;
    },
    category: function () {
      article = Session.get('ArticleDetails');
      return article.category;
    },
    pub_date: function () {
      article = Session.get('ArticleDetails');
      return article.pub_date;
    },
    author: function () {
      article = Session.get('ArticleDetails');
      return article.author;
    },
    text: function () {
      article = Session.get('ArticleDetails');
      return article.text;
    },
    Recommendations: function () {
      Recommendations = Session.get('Recommendations');
      return Recommendations;
  },
  
    
  });
  
  //event handlers
  
  //event handler for main template
  
  Template.main.events({
    
    // this handler is triggered from recommendations in the bottom nav bar
    //
    // it calls the getArticleDetails method that fetches more info on article
    //
    'click .read-more': function () {
      Meteor.call("getArticleDetails",this.id,function(error,result){
        Session.set("ArticleDetails",result[0].fields);
        recomArticleObjects = [];
        for (var i = 1; i <= result.length-1;i++){
            recomArticleObjects[i-1] = result[i].fields;
            recomArticleObjects[i-1].id = result[i].pk;
        }
        Session.set("Recommendations",recomArticleObjects);
      }); 
    },
    //this is just to take to home/landing page
    'click home-button':function(){
      Meteor.call("getRequest",function(error,result){
      Session.set("getResponse",result);
    });
    }
    
  });
  
  //event handler for landing template

  Template.landing.events({
    
    // this handler is triggered when user clicks read more button below article
    
    'click .read-more': function () {
      Session.setDefault("viewPage", "article");
      Meteor.call("getArticleDetails",this.id,function(error,result){
        Session.set("ArticleDetails",result[0].fields);
        recomArticleObjects = [];
        for (var i = 1; i <= result.length-1;i++){
            recomArticleObjects[i-1] = result[i].fields;
            recomArticleObjects[i-1].id = result[i].pk;
        }
        Session.set("Recommendations",recomArticleObjects);
      }); 
    },
    
    // triggered on submit of search bar
    
    'submit .search-bar':function(event){
      Meteor.call("getSearchResults",event.target.text.value,function(error,result){
        Session.set("getResponse",result);
      });
      return false;
    }
  });
  
  //event handler for landing template rendering complete
  
  Template.landing.rendered = function(){
    Meteor.call("getRequest",function(error,result){
      Session.set("getResponse",result);
    });
  }
}

if (Meteor.isServer) {
  Meteor.startup(function () {});
  
  //server methods ( to do GET requests)
  
  Meteor.methods({

  // this request gets all articles for list in landing page
  
  getRequest: function () {
    myJson = Meteor.http.call("GET", "http://127.0.0.1:8000/readerApp/landing/");
    articleObjects =[];
    for (var i = 0; i < myJson.data.length;i++){
      articleObjects[i] = myJson.data[i].fields
      articleObjects[i].id = myJson.data[i].pk
    }
    return articleObjects;
  },
  
  //this request gets all data for the calling article id
  
  getArticleDetails: function(id){
    myJson = Meteor.http.call("GET", "http://127.0.0.1:8000/readerApp/"+id+'/');
    return myJson.data;
  },
  
  //this request sends the search text as query parameter and gets the search results
  
  getSearchResults: function(text){
    text = encodeURIComponent(text);
    myJson = Meteor.http.call("GET", "http://127.0.0.1:8000/readerApp/search/",{params: {terms: text}});
    search_results =[];
    for (var i = 0; i < myJson.data.length;i++){
      search_results[i] = myJson.data[i].fields
      search_results[i].id = myJson.data[i].pk
    }
    return search_results;
  }
      
  });
}