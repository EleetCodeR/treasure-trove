#include <bits/stdc++.h>
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl

using namespace std;
// Do not edit the class below except for
// the insert, contains, and remove methods.
// Feel free to add new properties and methods
// to the class.
class BST
{
public:
    int value;
    BST *left;
    BST *right;

    BST(int val)
    {
        value = val;
        left = NULL;
        right = NULL;
    }

    BST &insert(int val)
    {
        // Write your code here.
        // Do not edit the return statement of this method.
        if (val < value)
        { //left
            if (left == NULL)
            {
                BST *newT = new BST(val);
                left = newT;
            }
            else
            {
                left->insert(val);
            }
        }
        else
        {
            //Right
            if (right == NULL)
            {
                BST *newT = new BST(val);
                right = newT;
            }
            else
            {
                right->insert(val);
            }
        }

        return *this;
    }

    bool contains(int val)
    {
        // Write your code here.
        if (val < value)
        { //left
            if (left == NULL)
            {
                return false;
            }
            else
            {
                return left->contains(val);
            }
        }
        else if (val > value)
        {
            //Right
            if (right == NULL)
            {
                return false;
            }
            else
            {
                return right->contains(val);
            }
        }
    }

    BST &remove(int val, BST *parent = NULL)
    {
        // only remove first occurance
        // can not remove from one node tree.

        //iteration
        if (val < value)
        {
            if (left != NULL)
                left->remove(val, this);
        }
        else if (val > value)
        {
            if (right != NULL)
                right->remove(val, this);
        }
        else
        { //deletion code

            if (left != NULL && right != NULL)
            { // 2 child
                value = right->minST();
                right->remove(value, this);
            }
            else if (parent == NULL)
            {
                if (left != NULL)
                {
                    value = left->value;
                    left = left->left;
                    right = left->right;
                }
                else if (right != NULL)
                {
                    value = right->value;
                    left = right->left;
                    right = right->right;
                }
                else
                {
                    // nothing
                }
            }
            else if (parent->left == this)
            {
                parent->left = left != NULL ? left : right;
            }
            else if (parent->right == this)
            {
                parent->right = left != NULL ? left : right;
            }
        }

        return *this;
    }

    int minST()
    {
        if (left == NULL)
        {
            return value;
        }
        else
        {
            return left->minST();
        }
    }
};

int main()
{
    // To Avoid input/output bottlenecks
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());

    return 0;
}