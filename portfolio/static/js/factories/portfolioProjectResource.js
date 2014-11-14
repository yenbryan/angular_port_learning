angPortfolio.factory('portfolioProject', function($resource){
    return $resource('http://127.0.0.1:8000/projects/', {
    },{
        update: {
            method: 'PUT'
//            'query': {method: 'GET', isArray: true}
        }
    });
});