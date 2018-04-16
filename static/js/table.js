var app = angular.module('rackspace-table-app', ['angularUtils.directives.dirPagination']);
app.controller('table-controller',function($scope, $http){
    $http.get("/getTableData").then(function(response){ 
        $scope.rows = response.data; 
        $scope.itemsPerPage = 10;
    });

    $scope.sort = function(keyname){
        $scope.sortKey = keyname;   
        $scope.reverse = !$scope.reverse; 
    }
});

