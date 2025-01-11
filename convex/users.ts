import { v } from "convex/values";
import { action, internalMutation, internalQuery, mutation, query } from "./_generated/server";

import { api, internal } from "./_generated/api";

export const store = mutation({
    args: {},
    handler: async (ctx) => {
        const identity = await ctx.auth.getUserIdentity();
        if (!identity) {
            throw new Error("Called storeUser without authentication present");
        }

        // Check if we've already stored this identity before.
        const user = await ctx.db
            .query("users")
            .withIndex("by_token", (q) =>
                q.eq("tokenIdentifier", identity.tokenIdentifier)
            )
            .unique();
        if (user !== null) {
            // If we've seen this identity before but the name has changed, patch the value.
            if (user.username !== identity.nickname) {
                await ctx.db.patch(user._id, { username: identity.nickname });
            }
            return user._id;
        }

        // If it's a new identity, create a new `User`.
        const userId = await ctx.db.insert("users", {
            fullName: identity.name!,
            tokenIdentifier: identity.tokenIdentifier,
            title: "",
            about: "",
            username: identity.nickname!,
            profileImageUrl: identity.profileUrl,
        });

        return userId;
    },
});


export const getCurrentUser = query({
    handler: async (ctx) => {
        const identity = await ctx.auth.getUserIdentity();

        if (!identity) {
            return null;
        }

        // throw new Error("Unauthenticated call to query");
        const user = await ctx.db
            .query("users")
            .withIndex("by_token", (q) =>
                q.eq("tokenIdentifier", identity.tokenIdentifier)
            )
            .unique();

        return user;
    }
});


export const get = query({
    args: { id: v.id("users") },
    handler: async (ctx, args) => {
        const user = await ctx.db.get(args.id);
        return user;
    },
});







export const getUserByUsername = query({
    args: { username: v.optional(v.string()) },
    handler: async (ctx, args) => {
        if (args.username === undefined) return null;
        if (!args.username) return null;
        const user = await ctx.db
            .query("users")
            .withIndex("by_username", (q) => q.eq("username", args.username!))
            .unique();

        return user;
    },
});



;