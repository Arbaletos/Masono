(function () {
  'use strict';

  angular.module('Masono', [])
  .controller('MasonoKontrolilo', ['$scope', '$log', '$http',
    function($scope, $log, $http) {
      var suc = function(results) {
            $scope.ret = results
          }
      var err = function(error) {
            $log.log(error);
          }
      $scope.ago= function(ago, dem_id) {
        $http.post('/send',{'ago':ago,'dem_id':dem_id}).
          success(suc).
          error(err);
      };
      $scope.sekv= function() {
        $http.get('/sekv').
          success(suc).
          error(err);
      };
    }
  ]);

}());