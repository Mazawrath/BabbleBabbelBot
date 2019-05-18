import collections
from credentials import username


# This is simple collection of functions to prevent reddit bots from:
# 1. replying twice to same summon
# 2. prevent chain of summons
# 3. have limit on number of replies per submission

# Note: See TODO and make according changes
# Note: You can use reply function like this: post_reply(comment-content,praw-comment-object)
# Note: is_summon_chain returns True if grandparent comment is bot's own
# Note: comment_limit_reached returns True if current will be 5th reply in same thread, resets on process restart
# Note: don't forget to decalre `submissioncount = collections.Counter()` before starting your main loop
# Note: Here, r = praw.Reddit('unique client identifier')

# def is_summon_chain(post, reddit):
#     if not post.is_root:
#         parent_comment_id = post.parent_id
#         parent_comment = reddit.get_info(thing_id=parent_comment_id)
#         if parent_comment.author != None and str(
#                 parent_comment.author.name) == username:
#             return True
#         else:
#             return False
#     else:
#         return False


def comment_limit_reached(post):
    global submission_count
    count_of_this = int(float(submission_count[str(post.submission.id)]))
    if count_of_this > 10:
        return True
    else:
        return False


def is_already_done(parent):
    done = False

    if parent.__class__.__name__ == 'Submission':
        # Post
        replies_array = parent.comments
    elif parent.__class__.__name__ == 'Comment':
        # Comment
        try:
            parent.refresh()
            replies_array = parent.replies
        except:
            pass
    else:
        raise AttributeError
    if len(replies_array) > 0:
        for reply in replies_array:
            if 'u/' + username.lower() in reply.body.lower():
                done = True
                break
    if done:
        return True
    else:
        return False


# def post_reply(reply, post):
#     global submission_count
#     try:
#         a = post.reply(reply)
#         submission_count[str(post.submission.id)] += 1
#         return True
#     except Exception as e:
#         warn("REPLY FAILED: %s @ %s" % (e, post.subreddit))
#         if str(e) == '403 Client Error: Forbidden':
#             print('/r/' + post.subreddit + ' has banned me.')
#             save_changing_variables()
#         return False


submission_count = collections.Counter()