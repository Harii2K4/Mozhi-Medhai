"use client";


import { Loading } from "@/components/auth/loading";
import { useAuth, RedirectToSignIn } from "@clerk/nextjs";
import { ConvexReactClient } from "convex/react";
import { ConvexProviderWithClerk } from "convex/react-clerk";
import { useEffect, useState } from "react";




interface ConvexClientProviderProps {
    children: React.ReactNode;
}

const convexUrl = process.env.NEXT_PUBLIC_CONVEX_URL!;

const convex = new ConvexReactClient(convexUrl);

export const ConvexClientProvider: React.FC<ConvexClientProviderProps> = ({ children }) => {
    const { isLoaded, isSignedIn } = useAuth();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (isLoaded) {
            setLoading(false);
        }
    }, [isLoaded]);

    if (loading) {
        return <Loading />;
    }

    if (!isSignedIn) {
        return <RedirectToSignIn />;
    }

    return (
        <ConvexProviderWithClerk useAuth={useAuth} client={convex}>
            {children}
            
        </ConvexProviderWithClerk>
    );
};