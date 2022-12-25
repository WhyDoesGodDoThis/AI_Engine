compile:
	javac src/*.java -d ./build -classpath ./build

archive: compile
	cd ./build/ && jar cvfe ../realms.jar entry *.class