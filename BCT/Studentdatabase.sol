// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentDatabase {

    struct Student {
        uint rollNo;
        string name;
        uint age;
        string course;
    }

    Student[] public students;

    function addStudent(
        uint _rollNo,
        string memory _name,
        uint _age,
        string memory _course
    ) public {
        students.push(
            Student(_rollNo, _name, _age, _course)
        );
    }

    function getStudent(uint _index)
        public
        view
        returns (
            uint,
            string memory,
            uint,
            string memory
        )
    {
        Student memory s = students[_index];

        return (
            s.rollNo,
            s.name,
            s.age,
            s.course
        );
    }

    function getStudentCount()
        public
        view
        returns (uint)
    {
        return students.length;
    }

    // Required fallback function
    fallback() external payable {
    }

    // Allows the contract to receive Ether directly
    receive() external payable {
    }
}