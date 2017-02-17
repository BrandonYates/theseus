using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace MazeProject
{
    public class Coord
    {
        public float x { get; set; }
        public float y { get; set; }
        public Coord(float x, float y)
        {
            this.x = x;
            this.y = y;
        }
    }
    public class Maze
    {
        public int length { get; set; }
        public int width { get; set; }
        public Section[,] sections { get; set; }
        public Coord start { get; set; }
        public Coord end { get; set; }

        public Maze(int len, int width)
        {
            length = len;
            this.width = width;
            sections = new Section[len, width];
            for(int x = 0; x < width; x++)
            {
                for(int y = 0; y < len; y++)
                {
                    sections[x, y] = new Section(x, y, true, true, true, true);
                }
            }

            start = new Coord(0, 0);
            end = new Coord(0, 0);
        }

        public void JoinSection(int x1, int x2, int y1, int y2)
        {
            var s1 = sections[y1, x1];
            var s2 = sections[y2, x2];

            var shared = Section.SharedWall(s1, s2);

            if (shared.Value == Section.Direction.North)
            {
                s2.OpenWall(Section.Direction.North);
                s1.OpenWall(Section.Direction.South);
            }
            else if (shared.Value == Section.Direction.South)
            {
                s2.OpenWall(Section.Direction.South);
                s1.OpenWall(Section.Direction.North);
            }
            else if (shared.Value == Section.Direction.East)
            {
                s2.OpenWall(Section.Direction.East);
                s1.OpenWall(Section.Direction.West);
            }
            else if (shared.Value == Section.Direction.West)
            {
                s2.OpenWall(Section.Direction.West);
                s1.OpenWall(Section.Direction.East);
            }
            else
            {
                Debug.LogError("'bad wall value returned by Section.sharedWall(): " + shared.Value);
            }

            sections[y1, x1] = s1;
            sections[y2, x2] = s2;

            return;
        }

        public bool CorrectPath(Section[] path)
        {
            if(path[0] == null || !(new Coord(path[0].x, path[0].y) == start))
            {
                return false;
            }

            if(path[path.Length - 1] == null || !(new Coord(path[0].x, path[0].y) == end))
            {
                return false;
            }

            for(int x = 0; x < path.Length - 2; x++)
            {
                if (!Section.ValidTransition(path[x], path[x + 1]))
                {
                    return false;
                }
            }

            return true;
        }

        public override string ToString()
        {
            string output = "";

            for(int y = 0; y < length; y++)
            {
                for(int z = 0; z < 3; z++)
                {
                    for(int x = 0; x < width; x++)
                    {
                        output += sections[y, x].GetRow(z);
                    }
                    output += "\n";
                }
            }

            return output;
        }
    }

    public class Section
    {
        public bool debug  { get; set; }
        public float x { get; set; }
        public float y { get; set; }
        public Dictionary<Direction, bool> walls { get; set; }

        public enum Direction { North, South, East, West };

        public Section(float x, float y, bool north, bool south, bool east, bool west, bool debug = false)
        {
            this.x = x;
            this.y = y;
            walls = new Dictionary<Direction, bool>();
            walls[Direction.North] = north;
            walls[Direction.South] = south;
            walls[Direction.East] = east;
            walls[Direction.West] = west;
            this.debug = debug;
        }

        public static Direction? SharedWall(Section s1, Section s2)
        {
            if (s1.debug || s2.debug)
            {
                Debug.Log("Is Adjacent");
                Debug.Log("x: " + s1.x.ToString() + " y: " + s1.y.ToString());
                Debug.Log("x: " + s2.x.ToString() + " y: " + s2.y.ToString());
            }

            if((s1.x + 1) == s2.x && s1.y == s2.y)
            {
                return Direction.East;
            }
            else if((s1.x - 1) == s2.x && s1.y == s2.y)
            {
                return Direction.West;
            }
            else if(s1.x == s2.x && (s2.y + 1) == s2.y)
            {
                return Direction.North;
            }
            else if(s1.x == s2.x && s1.y == (s2.y -1))
            {
                return Direction.South;
            }else
            {
                return null;
            }
        }

        public bool IsWallOpen(Direction d)
        {
            return !this.walls[d];
        }

        public void OpenWall(Direction d)
        {
            this.walls[d] = false;
        }

        public static bool ValidTransition(Section s1, Section s2)
        {
            var sharedWall = SharedWall(s1, s2);
            
            if(sharedWall == Direction.North)
            {
                return s1.IsWallOpen(Direction.North) && s2.IsWallOpen(Direction.South);
            }
            else if (sharedWall == Direction.South)
            {
                return s1.IsWallOpen(Direction.South) && s2.IsWallOpen(Direction.North);
            }
            else if (sharedWall == Direction.East)
            {
                return s1.IsWallOpen(Direction.East) && s2.IsWallOpen(Direction.West);
            }
            else if(sharedWall == Direction.West)
            {
                return s1.IsWallOpen(Direction.West) && s2.IsWallOpen(Direction.East);
            }
            else
            {
                return false;
            }
        }

        public string GetRow(int n)
        {
            if (n == 0)
            {
                return "*" + (walls[Direction.North] ? "*" : " ") + "*";
            }
            else if(n == 1)
            {
                return (walls[Direction.West] ? "*" : " ") + " " + (walls[Direction.East] ? "*" : " ");
            }
            else if (n == 2)
            {
                return "*" + (walls[Direction.South] ? "*" : " ") + "*";
            }
            else
            {
                return null;
            }
        }

        public void Dump()
        {
            Debug.Log("*" + (walls[Direction.North] ? "*" : " ") + "*");

            foreach(var item in walls)
            {
                Debug.Log(item.Key.ToString() + " " + item.Value.ToString());
            }
        }

        public override string ToString()
        {
            string output = "*";
            output += walls[Direction.North] ? "*" : " ";
            output += "*\n";
            output += walls[Direction.West] ? "*" : " ";
            output += " ";
            output += walls[Direction.East] ? "*" : " ";
            output += "\n*";
            output += walls[Direction.South] ? "*" : " ";
            output += "*";
            return output;
        }
    }
}

