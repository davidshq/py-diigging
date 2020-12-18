# The Diigo API

The Diigo API is pretty basic, its [documentation is contained on one brief page](diigoapi). This document reiterates much of what is covered there and hopefully a few other helpful additions.

# Fields Returned by API
Each bookmark is returned in the following format:
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

Notes:
- Bookmarks are stored as objects and comments/annotations are stored as arrays.
- Comments occur both at the level of the bookmark as well as individual annotations.
- I'm unclear on what the `"desc"` field contains, it seems like it could be page meta, but sometimes is nonsensical, urls, etc.
- Does `"shared"` mean public? I assume so at the moment.


[diigoapi]https://www.diigo.com/api_dev