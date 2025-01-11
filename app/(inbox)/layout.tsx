"use client";


import { Sidebar } from "./components/sidebar";
import ConversationList from "./components/sidebar/conversation-list";


export default function ConversationsLayout({
    children
}: {
    children: React.ReactNode,
}) {
    return (
        <>
            <div className="pt-[88px]">
                <Sidebar>
                    <div className="h-full">
                        <ConversationList />
                    </div>
                </Sidebar>
                <div className="h-full lg:pl-[300px]">
                    {children}
                </div>
            </div>

        </>
    );
}