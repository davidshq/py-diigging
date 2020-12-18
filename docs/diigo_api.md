# The Diigo API

## Introduction
The Diigo API is barebones and [all of its documentation](diigoapi) is contained on one brief page. This unofficial document seeks to augment and correct the information in the official API documentation.

## API Response
The Diigo API responds to valid queries with an array of bookmarks. An example bookmark (returned as an object) is shown below:

NOTE: The response from the API is almost inverted compared to that in the official docs.

NOTE: The comments/annotations associated with an individual bookmark are returned as an array.

```json
[
    {
        "readlater": "no",
        "tags": "some-tag, other-tag",
        "comments": [],
        "user": "someuser",
        "annotations": [
            {
                "content": "<p>Some content from the bookmarked page.</p>",
                "comments": [],
                "user": "someuser",
                "created_at": "2020/12/14 17:35:57 +0000"
            },
            {
                "content": "...",
                "comments": [],
                "user": "someuser",
                "created_at": "0000/00/00 00:00:00 +0000"
            }
        ],
        "url": "https://www.someurl.com/somepage",
        "shared": "yes",
        "created_at": "2020/12/14 17:35:57 +0000",
        "desc": "",
        "updated_at": "2020/12/14 17:36:39 +0000",
        "title": "Some Page Title"
    }
]
```

## API Field Meanings
- `readlater`: yes/no
- `tags`: for the bookmark, returned as a comma delimited string
- `comments`: on the bookmark level
- `user`: the user who saved the bookmark
- `annotations`: individual highlights and comments associated with the bookmark.
    - `content`: the highlighted text
    - `comments`: comments on this specific annotation
    - `user`: the user who created the annotation
    - `created_at`: time stamp
- `url`: the location of the bookmark
- `shared`: yes/no - whether the bookmark is public or private
- `created_at`: time stamp
- `desc`: Description entered by user
- `updated_at`: time stamp
- `title`: title of page, can be customized by user


[diigoapi]https://www.diigo.com/api_dev