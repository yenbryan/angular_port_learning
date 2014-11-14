var angPortfolio = angular.module('angPortfolio', [
    'ngRoute',
    'ngResource',
    'ngSanitize',
    'ui.bootstrap'
]);

angPortfolio.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        })
        .when('/my-follows/:userID', {
            templateUrl: '/static/js/views/my_follows.html',
            controller: myFollowsController
        })
        .when('/register', {
          templateUrl: '/static/js/views/auth.html',
          controller: authController
        })
//        .when('/my-follows/', {
//            templateUrl: '/static/js/views/my_follows.html',
//            controller: myFollowsController
//        })
        .otherwise({redirectTo: '/'});
}]);