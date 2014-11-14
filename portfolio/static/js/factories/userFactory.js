angPortfolio.factory('UserFactory', function($http, $routeParams) {
    return {
//        repoList: [],
        following: function(){
            console.log($routeParams);
//            return $http.post('http://127.0.0.1:8000/user/');
        }
    }
});