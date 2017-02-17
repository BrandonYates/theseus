using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using MazeProject;

public class MazeTester : MonoBehaviour {

	// Use this for initialization
	void Start () {
        var maze = new Maze(2, 2);
        Debug.Log(maze.sections[0,0].ToString());
        Debug.Log("Adjacent? " + Section.SharedWall(maze.sections[0, 0], maze.sections[1, 0]).Value.ToString());

        var openSection = new Section(4, 4, false, false, false, false);
        var closedSection = new Section(4, 5, true, true, true, true);

        Debug.Log(openSection.ToString());

        Debug.Log(closedSection.ToString());

        Debug.Log("Valid Transition: " + Section.ValidTransition(openSection, closedSection).ToString());

        var shared = Section.SharedWall(closedSection, openSection);

        if (shared.HasValue)
        {
            Debug.Log(shared.Value.ToString());
            closedSection.OpenWall(shared.Value);
        }
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
