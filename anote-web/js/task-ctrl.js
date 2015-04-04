var phonecatApp = angular.module('phonecatApp', [])

var TAG_API_URL = '/apiv1/tag';
var PROJECT_API_URL = '/apiv1/project';
var TASK_API_URL = '/apiv1/task';

phonecatApp.directive('autoComplete', function($timeout) {
    return function(scope, iElement, iAttrs) {
            iElement.autocomplete({
                source: scope[iAttrs.uiItems],
                select: function() {
                    $timeout(function() {
                      iElement.trigger('input');
                    }, 0);
                }
            });
    };
});


phonecatApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'html/task-list.html',
        controller: 'TaskCtrl',
      }).
      when('/new', {
        templateUrl: 'html/task-new.html',
        controller: 'NewTaskCtrl',
      }).
      when('/task/:id', {
        templateUrl: 'html/task-detail.html',
        controller: 'TaskDetailCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);


phonecatApp.controller('TaskCtrl', ['$scope', '$http', '$timeout',
  function($scope, $http, $timeout) {
    $scope.refresh_func = function() {
      $http.get(TAG_API_URL).success(function(data) {
        $timeout(function() {
          $scope.tags = data;
        });
      });

      $http.get(PROJECT_API_URL).success(function(data) {
        $timeout(function() {
          $scope.projects = data;
        });
      });
    };

    $scope.addTag = function(newTag) {
      tagModel = {}
      tagModel.tag_name = newTag;
      $http.post(TAG_API_URL, angular.toJson(tagModel)).success(function(data) {
        $scope.tag_success = 'success';
        $scope.tags.push(data);
      });
      $scope.newTag = "";
    };

    $scope.removeTag = function(tagKey) {
      $http.delete(TAG_API_URL, {params: {'key': tagKey}}).success(function(data) {
        $timeout(function() {
          for (i=0; i<$scope.tags.length; i++) {
            if ($scope.tags[i].key === tagKey) {
              $scope.tags.splice(i, 1);
              break;
            }
          }
        });
      });
    };

    $scope.addProject = function(newProject) {
      projectModel = {}
      projectModel.project_name =  newProject;
      $http.post(PROJECT_API_URL, angular.toJson(projectModel)).success(function(data) {
        $scope.projects.push(data);
      });

      $scope.newProject = "";
    };

    $scope.removeProject = function(projectKey) {
      $http.delete(PROJECT_API_URL, {params: {'key': projectKey}}).success(function(data) {
        $timeout(function() {
          for (i=0; i<$scope.projects.length; i++) {
            if ($scope.projects[i].key === projectKey) {
              $scope.projects.splice(i, 1);
              break;
            }
          }
        });
      });
    };

    // table related.
    $scope.columns_meta = [
      {"col_name": "priority", "display_name": "P", "attr_name": "priority"},
      {"col_name": "title", "display_name": "TITLE", "attr_name": "title"},
      {"col_name": "status", "display_name": "STATUS", "attr_name": "status"},
      {"col_name": "last_modification", "display_name": "LAST MODIFIED", "attr_name": "last_modification"}
    ];
    $scope.column_sorted_class = "array-up";
    $scope.column_sorted_currrent = "priority";

    (function() {
      $scope.refresh_func();
    })();

}]);

phonecatApp.controller('NewTaskCtrl', ['$scope', '$http', '$timeout',
  function($scope, $http, $timeout) {
    $scope.addTask = function(newTask) {
      taskModel = {};
      taskModel.title = newTask.title;

      note = {};
      note.text = newTask.note;
      taskModel.notes = []
      taskModel.notes.push(note);

      taskModel.project = newTask.project;
      taskModel.priority = newTask.priority;
      taskModel.status = 'new';

      $http.put(TASK_API_URL, angular.toJson(taskModel)).success(function(data) {
        $scope.projects.push(data);
      });

      $scope.newProject = "";
    };

  }]);

phonecatApp.controller('TaskDetailCtrl', ['$scope', '$http', '$route',
  function($scope, $http, $route) {

    $scope.refresh_func = function() {
      url = TASK_API_URL + "?taskId=" + $route.current.params['id'];
      $http.get(url).success(function(data) {
        $timeout(function() {
          $scope.task = data;
        });
      });

    };
    $scope.title = "abc";
      $scope.task = {
        'title': 'Title Text',
        'notes': [{
          'text': 'note text1',
          'createAt': 1000,
          'commentNumber': 1
        }, {
          'text': 'note text2',
          'createAt': 1001,
          'commentNumber': 2
        }]
      };

    (function() {
      $scope.refresh_func();
    })();
  }]);

function TaskCtrl2($scope) {


  $scope.addTask = function() {
    $scope.tasks.push({taskText:$scope.taskInputText, done:false});
    $scope.taskInputText = '';
  };

  $scope.remaining = function() {
    var count = 0;
    var a = 3 + 2

    angular.forEach($scope.todos, function(todo) {
      count += todo.done ? 0 : 1;
    });
    return count;
  };

  $scope.archive = function() {
    var oldTodos = $scope.todos;
    $scope.todos = [];
    angular.forEach(oldTodos, function(todo) {
      if (!todo.done) $scope.todos.push(todo);
    });
  };
}

